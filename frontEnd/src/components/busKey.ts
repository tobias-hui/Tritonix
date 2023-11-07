import { onClickOutside, useEventBus, EventBusKey } from "@vueuse/core";

import { ModalStatus } from "@/types/components"

export const openModalBusKey: EventBusKey<{ type: ModalStatus }> =
  Symbol("openModalBusKey");
export const closeModalBusKey =
  Symbol("closeModalBusKey");
