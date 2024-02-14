#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(9, function () {
  console.log('C is fun');
});
