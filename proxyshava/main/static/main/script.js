let currentDomain = '';

const serverConfigs = {
  '🧪Новичок сервер': {
    ip: '104.128.137.29',
    port: 443,
    key: 'bda6be5694ece53c7a90b8468530d0f0'
  },
  '🪆Катюша сервер': {
    ip: '81.200.146.184',
    port: 443,
    key: 'd88b1b24399ae5d3b7df62be5576fbb3'
  },
  '🧸Медведи сервер': {
    ip: '104.128.137.28',
    port: 443,
    key: '5486dab699f041e1e5c913005808d4dc'
  },
  '🌕Луна сервер': {
    ip: '0.0.0.0',
    port: 0,
    key: ''
  },
  '🍔Бургер сервер': {
    ip: '0.0.0.0',
    port: 0,
    key: ''
  },
};

function checkServers() {
  const now = new Date();
  document.getElementById('updateTime').innerText = 'Обновлено: ' + now.toLocaleTimeString();
}
setInterval(checkServers, 30000);
checkServers();

function updateServerStatus(serverNumber, isOnline) {
  const statusDot = document.getElementById('status' + serverNumber);
  if (statusDot) {
    if (isOnline) {
      statusDot.classList.remove('offline');
      statusDot.classList.add('online');
    } else {
      statusDot.classList.remove('online');
      statusDot.classList.add('offline');
    }
  }
}

function autoScroll() {
  const viewportHeight = window.innerHeight;
  const documentHeight = document.body.scrollHeight;
  const targetPosition = documentHeight - (viewportHeight * 1.5);
  window.scrollTo({ top: targetPosition, behavior: 'smooth' });
}

function showQRCode(link, domain) {
  currentDomain = domain;
  document.getElementById('selectedDomain').innerText = 'Выбран домен: ' + domain;
  autoScroll();
  const container = document.getElementById('qrCodeContainer');
  container.style.display = 'block';
  container.classList.remove('hidden');
  setTimeout(() => {
    container.classList.add('show');
  }, 10);
  const qrCanvas = document.getElementById('qrCode');
  QRCode.toCanvas(qrCanvas, link, { width: 200 }, function (error) {
    if (error) console.error(error);
  });
}

function showSettings(serverId) {
  document.getElementById('settingsText').innerText = 'Настройки для ' + serverId;
  const config = serverConfigs[serverId] || { ip: '', port: '', key: '' };
  document.getElementById('settingsIp').value = config.ip;
  document.getElementById('settingsPort').value = config.port;
  document.getElementById('settingsKey').value = config.key;
  document.getElementById('settingsModal').style.display = 'flex';
}

function closeSettings() {
  document.getElementById('settingsModal').style.display = 'none';
}

// Обновление статусов, пример:
updateServerStatus(0, true);
updateServerStatus(1, true);
updateServerStatus(2, true);
updateServerStatus(3, false);
updateServerStatus(4, false);

// Создайте плавающую кнопку подписки
document.addEventListener('DOMContentLoaded', () => {
  const subscribeBtn = document.createElement('div');
  subscribeBtn.className = 'subscribe-btn';
  subscribeBtn.innerHTML = '<i class="fas fa-user-plus"></i>';
  document.body.appendChild(subscribeBtn);
  subscribeBtn.onclick = () => {
    window.open('https://t.me/proxyshava', '_blank');
  };
});
