export default function getListStudentIds(stlist) {
  try {
    return stlist.map((mapped) => mapped.id);
  } catch (error) {
    return [];
  }
}
