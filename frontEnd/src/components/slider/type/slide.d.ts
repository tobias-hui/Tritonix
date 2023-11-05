export interface SlideState {
  currentIndex: number;
  start: {
    x: number;
    y: number;
  };
  isMouseDown: boolean;
  move: {
    x: number;
    y: number;
  };
  wrapper: {
    width: number;
    height: number;
    childrenLength: number;
  };
  lastTransition: {
    x: number;
    y: number;
  };
  transition: {
    x: number;
    y: number;
  };
  durationTime: number;
  mouseDownTimeStamp: number;
}