document.addEventListener('DOMContentLoaded', function() {
    updateCharts('creditcard.csv', 'creditcardPieChart', 'creditcardBarChart');
    updateCharts('filtered_creditcard.csv', 'filteredCreditcardPieChart', 'filteredCreditcardBarChart');
});

async function fetchData(dataset) {
    const response = await fetch(`/statistics/${dataset}`);
    const data = await response.json();
    return data;
}

async function updateCharts(dataset, pieChartId, barChartId) {
    const data = await fetchData(dataset);

    const pieCtx = document.getElementById(pieChartId).getContext('2d');
    const barCtx = document.getElementById(barChartId).getContext('2d');

    // // Destroy existing charts if they exist
    if (window[pieChartId] instanceof Chart) window[pieChartId].destroy();
    if (window[barChartId] instanceof Chart) window[barChartId].destroy();

    // Create pie chart 
    window[pieChartId] = new Chart(pieCtx, {
        type: 'pie',
        data: {
            labels: ['Fraudulent', 'Non-Fraudulent'],
            datasets: [{
                data: [data.fraudulent, data.nonFraudulent],
                backgroundColor: ['#FF6384', '#36A2EB']
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Fraudulent vs Non-Fraudulent Transactions'
                }
            }
        }
    });

    // Create bar chart
    window[barChartId] = new Chart(barCtx, {
        type: 'bar',
        data: {
            labels: ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28'],
            datasets: [{
                label: 'Average Value',
                data: data.averageValues,
                backgroundColor: '#36A2EB'
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Average Values of Features'
                }
            }
        }
    });
}