#!/usr/bin/node
if (process.argv[2] !== undefined && process.argv[3] !== undefined) { console.log('Arguments found'); } else if (process.argv[2] !== undefined && process.argv[3] === undefined) { console.log('Argument found'); } else { console.log('No argument'); }
