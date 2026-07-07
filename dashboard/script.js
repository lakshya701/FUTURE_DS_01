// Fetch and display dashboard data
let dashboardData = null;

// Load data from JSON file
async function loadData() {
    try {
        const response = await fetch('../data/dashboard_data.json');
        dashboardData = await response.json();
        renderDashboard();
    } catch (error) {
        console.error('Error loading data:', error);
        document.body.innerHTML = '<h1>⚠️ Error: Could not load dashboard data</h1><p>Run: python src/analysis.py</p>';
    }
}

// Render all dashboard components
function renderDashboard() {
    if (!dashboardData) return;
    
    displayKPIs();
    displayMonthlyChart();
    displayCategoryChart();
    displayRegionChart();
    displaySegmentChart();
    displayTopProducts();
    displaySeasonalityChart();
    displayInsights();
}

// Display KPI cards
function displayKPIs() {
    const kpi = dashboardData.kpi;
    document.getElementById('revenue').textContent = `₹${(kpi.revenue / 10000000).toFixed(2)}Cr`;
    document.getElementById('profit').textContent = `₹${(kpi.profit / 100000).toFixed(2)}L`;
    document.getElementById('margin').textContent = `${kpi.margin}%`;
    document.getElementById('orders').textContent = kpi.orders.toLocaleString();
    document.getElementById('aov').textContent = `₹${Math.round(kpi.aov).toLocaleString()}`;
}

// Monthly revenue and profit chart
function displayMonthlyChart() {
    const ctx = document.getElementById('monthlyChart').getContext('2d');
    const data = dashboardData.monthly;
    
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.labels,
            datasets: [
                {
                    label: 'Revenue',
                    data: data.revenue,
                    borderColor: '#667eea',
                    backgroundColor: 'rgba(102, 126, 234, 0.1)',
                    tension: 0.4,
                    fill: true
                },
                {
                    label: 'Profit',
                    data: data.profit,
                    borderColor: '#764ba2',
                    backgroundColor: 'rgba(118, 75, 162, 0.1)',
                    tension: 0.4,
                    fill: true
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: { position: 'top' }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    title: { display: true, text: 'Amount (₹)' }
                }
            }
        }
    });
}

// Category performance chart
function displayCategoryChart() {
    const ctx = document.getElementById('categoryChart').getContext('2d');
    const data = dashboardData.category;
    
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: [
                {
                    label: 'Revenue',
                    data: data.revenue,
                    backgroundColor: '#667eea'
                },
                {
                    label: 'Profit',
                    data: data.profit,
                    backgroundColor: '#764ba2'
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: 'top' }
            }
        }
    });
}

// Region performance chart
function displayRegionChart() {
    const ctx = document.getElementById('regionChart').getContext('2d');
    const data = dashboardData.region;
    
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: [
                {
                    label: 'Revenue',
                    data: data.revenue,
                    backgroundColor: '#667eea'
                },
                {
                    label: 'Profit',
                    data: data.profit,
                    backgroundColor: '#764ba2'
                }
            ]
        },
        options: {
            indexAxis: 'y',
            responsive: true
        }
    });
}

// Customer segment chart
function displaySegmentChart() {
    const ctx = document.getElementById('segmentChart').getContext('2d');
    const data = dashboardData.segment;
    
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: data.labels,
            datasets: [{
                data: data.revenue,
                backgroundColor: ['#667eea', '#764ba2', '#f093fb', '#4facfe']
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: 'right' }
            }
        }
    });
}

// Top products table
function displayTopProducts() {
    const data = dashboardData.top_products;
    let html = '<table><thead><tr><th>Product</th><th>Revenue</th><th>Profit</th></tr></thead><tbody>';
    
    data.labels.forEach((label, i) => {
        html += `<tr><td>${label}</td><td>₹${Math.round(data.revenue[i]).toLocaleString()}</td><td>₹${Math.round(data.profit[i]).toLocaleString()}</td></tr>`;
    });
    
    html += '</tbody></table>';
    document.getElementById('topProductsTable').innerHTML = html;
}

// Seasonality chart
function displaySeasonalityChart() {
    const ctx = document.getElementById('seasonalityChart').getContext('2d');
    const data = dashboardData.seasonality;
    
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: [{
                label: 'Revenue',
                data: data.revenue,
                backgroundColor: '#667eea'
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false }
            }
        }
    });
}

// Display key insights
function displayInsights() {
    const insights = [
        { title: '🌟 Technology is the Winner', text: 'Technology has 14.8% profit margin vs Furniture\'s 2.3%. Focus marketing on Tech products.' },
        { title: '📉 Revenue Declining', text: 'Revenue dropped 12% from 2009-2011. Need to investigate customer retention and pricing.' },
        { title: '👑 Ontario Leads', text: 'Ontario has 11.3% margin vs West\'s 8.3%. Study their practices and apply elsewhere.' },
        { title: '💎 Corporate is Gold', text: 'Corporate segment generates ₹60L profit - more than other segments combined.' },
        { title: '🎄 December Peak', text: 'December and January are 30% above average. Stock up and plan staffing for Q4.' },
        { title: '⚠️ Tables Lose Money', text: 'Tables and Bookcases are loss-makers. Renegotiate supplier costs urgently.' }
    ];
    
    let html = '';
    insights.forEach(insight => {
        html += `<div class="insight-item"><strong>${insight.title}:</strong> ${insight.text}</div>`;
    });
    
    document.getElementById('insightsContainer').innerHTML = html;
}

// Load data on page load
window.addEventListener('DOMContentLoaded', loadData);
