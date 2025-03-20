// Hydrogen ↔ Power Calculator
async function calculatePower() {
    const hydrogen = document.getElementById('hydrogenInput').value;
    const response = await fetch('/calculate_power', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ hydrogen: hydrogen })
    });
    const data = await response.json();
    document.getElementById('powerResult').innerHTML = `Power: ${data.power} kW`;
}

async function calculateHydrogen() {
    const power = document.getElementById('powerInput').value;
    const response = await fetch('/calculate_hydrogen', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ power: power })
    });
    const data = await response.json();
    document.getElementById('hydrogenResult').innerHTML = `Hydrogen Needed: ${data.hydrogen} kg`;
}

// Task Converter
async function convertTask() {
    const task = document.getElementById('taskInput').value;
    const response = await fetch('/convert_task', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ task: task })
    });
    const data = await response.json();
    if (data.error) {
        document.getElementById('taskResult').innerHTML = data.error;
    } else {
        document.getElementById('taskResult').innerHTML = `Hydrogen Needed: ${data.hydrogen} kg`;
    }
}

// Production Method Comparison
async function compareMethods() {
    const method = document.getElementById('methodInput').value;
    const response = await fetch('/compare_methods', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ method: method })
    });
    const data = await response.json();
    if (data.error) {
        document.getElementById('impactResult').innerHTML = data.error;
    } else {
        document.getElementById('impactResult').innerHTML = 
            `Cost: $${data.cost}/kg | CO₂ Emissions: ${data.co2} kg/kg H₂`;
    }
}