#!/usr/bin/node
function call (x, theFunction) {
  for (let i = 0; i < x; ++i) {
    theFunction();
  }
}
exports.callMeMoby = call;
