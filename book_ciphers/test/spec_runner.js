var Jasmine = require('jasmine'),
  reporters = require('jasmine-reporters');

var jasmine = new Jasmine();
var reporter = {
  specDone: function (result) {
    console.log(`
      [${result.fullName}]

      Tests       Results
      -------     --------------
      ${result.description}     ${result.status}
    `);
  }
};

jasmine.loadConfigFile("./test/jasmine.json");
jasmine.addReporter(reporter);
jasmine.execute();
