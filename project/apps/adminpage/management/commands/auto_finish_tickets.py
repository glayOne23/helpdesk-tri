from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db import transaction
from datetime import timedelta

from apps.adminpage.models import Ticket, TicketState
from apps.adminpage.models.ticketing.m_ticketstatedetail import TicketStateDetail


class Command(BaseCommand):
    help = 'Otomatis mengubah state tiket dari in_process menjadi finish jika sudah lebih dari 2 minggu'

    def handle(self, *args, **options):
        batas_waktu = timezone.now() - timedelta(weeks=2)

        # Tiket yang sedang in_process dan entri in_process terakhirnya sudah > 2 minggu
        tiket_list = Ticket.objects.filter(
            state__code='in_process',
            ticketstatedetail__state__code='in_process',
            ticketstatedetail__created_at__lte=batas_waktu,
        ).distinct()

        if not tiket_list.exists():
            self.stdout.write(self.style.SUCCESS('Tidak ada tiket yang perlu diubah.'))
            return

        state_finish = TicketState.get_finish()
        jumlah = 0

        with transaction.atomic():
            for tiket in tiket_list:
                # Pastikan entri in_process TERBARU memang sudah > 2 minggu
                entri_terakhir = (
                    TicketStateDetail.objects
                    .filter(ticket=tiket, state__code='in_process')
                    .order_by('-id')
                    .first()
                )
                if entri_terakhir and entri_terakhir.created_at <= batas_waktu:
                    tiket.state = state_finish
                    tiket.save()
                    TicketStateDetail.objects.create(
                        ticket=tiket,
                        state=state_finish,
                        user=None,
                    )
                    jumlah += 1
                    self.stdout.write(f'  Tiket #{tiket.id} "{tiket.title}" -> finish')

        self.stdout.write(self.style.SUCCESS(f'Selesai: {jumlah} tiket diubah menjadi finish.'))
