const Jasmine = require('jasmine');

const jasmine = new Jasmine();
const reporter = {
  specDone: (result) => {
    console.log(`
      [${result.fullName.split(' ')[0]}]

      Results      Tests
      --------     --------------
      ${result.status}       ${result.description}
    `);
  }
};

jasmine.loadConfigFile('./tests/jasmine.json');
jasmine.addReporter(reporter);
jasmine.execute();
