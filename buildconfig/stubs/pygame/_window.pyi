from typing import Iterable, Optional, Tuple, Union, final
from pygame.surface import Surface
from ._common import RectValue
from pygame.locals import WINDOWPOS_UNDEFINED

def get_grabbed_window() -> Optional[Window]: ...
@final
class Window:
    def __init__(
        self,
        title: str = "pygame window",
        size: Iterable[int] = (640, 480),
        position: Union[int, Iterable[int]] = WINDOWPOS_UNDEFINED,
        **flags: bool
    ) -> None: ...
    def destroy(self) -> None: ...
    def set_windowed(self) -> None: ...
    def set_fullscreen(self, desktop: bool = False) -> None: ...
    def focus(self, input_only: bool = False) -> None: ...
    def hide(self) -> None: ...
    def show(self) -> None: ...
    def restore(self) -> None: ...
    def maximize(self) -> None: ...
    def minimize(self) -> None: ...
    def set_modal_for(self, parent: Window) -> None: ...
    def set_icon(self, icon: Surface) -> None: ...
    grab: bool
    title: str
    resizable: bool
    borderless: bool
    relative_mouse: bool
    id: int
    size: Iterable[int]
    position: Union[int, Iterable[int]]
    opacity: float
    display_index: int
    @classmethod
    def from_display_module(cls) -> Window: ...
