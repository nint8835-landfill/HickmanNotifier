from typing import Dict

from PyHickmanSales.vehicle import Vehicle

from .TwitterNotifier import TwitterNotifier


class VehicleCollection:

    _vehicles: Dict[str, Vehicle]
    _notifier: TwitterNotifier

    def __init__(self):
        self._vehicles = {}
        self._notifier = TwitterNotifier()

    def __getitem__(self, vin: str) -> Vehicle:
        return self._vehicles[vin]

    def __setitem__(self, vin: str, new_vehicle: Vehicle) -> None:
        if vin not in self._vehicles:
            self._notifier.notify(None, new_vehicle)

        else:
            if self._vehicles[vin].price != new_vehicle.price:
                self._notifier.notify(self._vehicles[vin], new_vehicle)

        self._vehicles[vin] = new_vehicle
