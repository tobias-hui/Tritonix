import { v4 as uuidv4 } from "uuid";

export default function getUid() {
  const uid = uuidv4();
  return uid;
}
