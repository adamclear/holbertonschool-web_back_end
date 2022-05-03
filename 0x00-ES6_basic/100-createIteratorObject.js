export default function createIteratorObject(report) {
  const reporter = report.allEmployees;
  const empIterator = {
    deptnum: 0,
    empnum: 0,
    next() {
      const keys = Object.keys(reporter);
      if (keys[this.deptnum]) {
        if (reporter[keys[this.deptnum]][this.empnum]) {
          const addemp = {
            value: reporter[keys[this.deptnum]][this.empnum],
            done: false,
          };
          this.empnum += 1;
          return addemp;
        }
        this.deptnum += 1;
        this.empnum = 0;
        return this.next();
      }
      return { value: null, done: true };
    },
    [Symbol.iterator]() {
      return this;
    },
  };
  return empIterator;
}
