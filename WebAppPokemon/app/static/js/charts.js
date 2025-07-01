fetch('/api/serie')
  .then(response => response.json())
  .then(data => {
    const ctx = document.getElementById('lineChart').getContext('2d');
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: data.anni,
        datasets: [{
          label: 'Valori',
          data: data.valori,
          borderColor: 'rgba(75, 192, 192, 1)',
          fill: false,
          tension: 0.1
        }]
      }
    });
  });

fetch('/api/pokemon/type1')
  .then(response => response.json())
  .then(data => {
    const ctx = document.getElementById('typeChart').getContext('2d');
    new Chart(ctx, {
      type: 'pie',
      data: {
        labels: data.labels,
        datasets: [{
          label: 'Distribuzione Type1',
          data: data.counts,
          backgroundColor: [
            'rgba(255, 99, 132, 0.6)',
            'rgba(54, 162, 235, 0.6)',
            'rgba(255, 206, 86, 0.6)',
            'rgba(75, 192, 192, 0.6)',
            'rgba(153, 102, 255, 0.6)',
            'rgba(255, 159, 64, 0.6)',
            'rgba(201, 203, 207, 0.6)',
            'rgba(100, 200, 100, 0.6)',
            'rgba(200, 100, 200, 0.6)',
            'rgba(100, 100, 200, 0.6)',
            'rgba(200, 200, 100, 0.6)',
            'rgba(100, 200, 200, 0.6)',
            'rgba(200, 100, 100, 0.6)',
            'rgba(150, 150, 150, 0.6)',
            'rgba(50, 50, 50, 0.6)'
          ]
        }]
      }
    });
  });

// Grafico a barre: media HP per type1
fetch('/api/pokemon/hp_media_type1')
  .then(response => response.json())
  .then(data => {
    const ctx = document.getElementById('hpChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: data.labels,
        datasets: [{
          label: 'Media HP per Type1',
          data: data.media,
          backgroundColor: 'rgba(255, 99, 132, 0.6)'
        }]
      },
      options: {
        indexAxis: 'y',
        scales: {
          x: {
            beginAtZero: true
          }
        }
      }
    });
  });

  fetch('/api/pokemon/attack_media_type1')
    .then(response => response.json())
  .then(data => {
    const ctx = document.getElementById('attChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: data.labels,
        datasets: [{
          label: 'Media Attacco per Type1',
          data: data.media,
          backgroundColor: 'rgba(255, 99, 132, 0.6)'
        }]
      },
      options: {
        indexAxis: 'y',
        scales: {
          x: {
            beginAtZero: true
          }
        }
      }
    });
  });

// Card: leggendario con più attacco e più difesa
fetch('/api/pokemon/legendary/top_stats')
  .then(response => response.json())
  .then(data => {
    const card = document.getElementById('legendaryCard');
    if (!data.max_attack || !data.max_defense) {
      card.innerHTML = '<b>Nessun dato disponibile sui Pokémon leggendari.</b>';
      return;
    }
    card.innerHTML = `
      <h3>Pokémon Leggendari: Top Attacco e Difesa</h3>
      <div><b>Attacco:</b> ${data.max_attack.name} (${data.max_attack.attack}) [${data.max_attack.type1}${data.max_attack.type2 ? ' / ' + data.max_attack.type2 : ''}]</div>
      <div><b>Difesa:</b> ${data.max_defense.name} (${data.max_defense.defense}) [${data.max_defense.type1}${data.max_defense.type2 ? ' / ' + data.max_defense.type2 : ''}]</div>
    `;
  });

// Grafico a torta: distribuzione type1 dei leggendari
fetch('/api/pokemon/legendary/type1_distribution')
  .then(response => response.json())
  .then(data => {
    const ctx = document.getElementById('legendaryTypeChart').getContext('2d');
    new Chart(ctx, {
      type: 'pie',
      data: {
        labels: data.labels,
        datasets: [{
          label: 'Type1 Leggendari',
          data: data.counts,
          backgroundColor: [
            'rgba(255, 99, 132, 0.6)',
            'rgba(54, 162, 235, 0.6)',
            'rgba(255, 206, 86, 0.6)',
            'rgba(75, 192, 192, 0.6)',
            'rgba(153, 102, 255, 0.6)',
            'rgba(255, 159, 64, 0.6)',
            'rgba(201, 203, 207, 0.6)',
            'rgba(100, 200, 100, 0.6)',
            'rgba(200, 100, 200, 0.6)',
            'rgba(100, 100, 200, 0.6)',
            'rgba(200, 200, 100, 0.6)',
            'rgba(100, 200, 200, 0.6)',
            'rgba(200, 100, 100, 0.6)',
            'rgba(150, 150, 150, 0.6)',
            'rgba(50, 50, 50, 0.6)'
          ]
        }]
      }
    });
  });
