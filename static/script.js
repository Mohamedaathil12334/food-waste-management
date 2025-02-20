document.getElementById('wasteForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    fetch('/add', {
        method: 'POST',
        body: formData
    }).then(response => {
        if (response.redirected) {
            window.location.href = response.url;
        }
    });
});

// Fetch data and render chart
fetch('/data')
    .then(response => response.json())
    .then(data => {
        const labels = data.map(entry => entry.date);
        const quantities = data.map(entry => parseFloat(entry.quantity));

        const ctx = document.getElementById('wasteChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Food Waste (kg)',
                    data: quantities,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    });