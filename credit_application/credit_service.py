from credit_application.models import CreditApplication


class CreditService:

    @staticmethod
    def get_producers_by_contract_id(contract_id: int) -> list[int]:
        return list(
            CreditApplication.objects.filter(
                contract=contract_id,
            ).values_list(
                'products__producer',
                flat=True,
            ).distinct(),
        )
