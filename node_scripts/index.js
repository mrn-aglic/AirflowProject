class DataManager {
    #name;

    constructor(name) {
        this.#name = name;
    }

    getName() {
        return `Hello, my name is: ${this.#name}`;
    }
}

function run() {
    const dataManager = new DataManager('Test')
    console.log('running')
    return dataManager.getName();
}

module.exports = {
    run
};

const value = run();
console.log({result: value});
return {result: value};

// return runApi();
// run().then(res => console.log('script success')).catch(err => console.log(err));