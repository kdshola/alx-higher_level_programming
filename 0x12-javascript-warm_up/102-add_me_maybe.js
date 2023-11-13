#!/usr/bin/node
function addAndCall (number, theFunction) {
  theFunction(++number);
}
exports.addMeMaybe = addAndCall;
