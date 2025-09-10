from PySide6.QtCore import QThread, Signal, Slot, QTimer

class Worker(QThread):
    result = Signal(str)
    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self._func = func
        self._args = args
        self._kwargs = kwargs

    def run(self, ):
        try:
            QTimer.singleShot(3000, Slot(self._func(*self._args, **self._kwargs)))
            self.result.emit('Задача завершена!')
        except Exception as err:
            self.result.emit(f'Error: {err}')
