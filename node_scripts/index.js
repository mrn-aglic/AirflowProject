class DataManager {
    #name;

    constructor(name) {
        this.#name = name;
    }

    getName() {
        return `Hello, my name is: ${this.#name}`;
    }
}

async function run() {
    const dataManager = new DataManager('Test')
    console.log('running')
    return dataManager.getName();
}

function runApi() {
    run().then(res => console.log(res));
}

module.exports = {
    runApi,
    run
};

// runApi();

// return runApi();
// run().then(res => console.log('script success')).catch(err => console.log(err));