#!/usr/bin/node

exports.esrever = function (list) {
  const newList = list.map((item, index) => list[list.length - 1 - index]);
  return newList;
};
