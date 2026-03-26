let currentDomain = '';

  // Объект с конфигурациями серверов
  const serverConfigs = {
    '🪆Катюша сервер': {
      ip: '81.200.146.184',
      port: 443,
      key: 'd88b1b24399ae5d3b7df62be5576fbb3'
    },
    '🧸Русский медведь сервер': {
      ip: '0.0.0.0',
      port: 0,
      key: ''
    },
    '🌕Луна сервер': {
      ip: '0.0.0.0',
      port: 0,
      key: ''
    }
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

  function showQRCode(link, domain) {
    currentDomain = domain;
    document.getElementById('selectedDomain').innerText = 'Выбран домен: ' + domain;
    window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
    const container = document.getElementById('qrCodeContainer');
    container.style.display = 'block';
    container.classList.remove('show');
    setTimeout(() => {
      container.classList.add('show');
    }, 10);
    const qrCanvas = document.getElementById('qrCode');
    QRCode.toCanvas(qrCanvas, link, { width: 200 }, function (error) {
      if (error) console.error(error);
    });
  }

  function connectTelegram() {
    // Используем параметры текущего сервера для ссылки
    const config = serverConfigs['🪆Катюша сервер'];
    if (config) {
      const url = `https://t.me/proxy?server=${config.ip}&port=${config.port}&secret=${config.key}`;
      window.open(url, '_blank');
    }
  }

  function showSettings(serverId) {
    document.getElementById('settingsText').innerText = 'Настройки для ' + serverId;
    // Получаем конфиг
    const config = serverConfigs[serverId] || { ip: '', port: '', key: '' };
    // Заполняем поля
    document.getElementById('settingsIp').value = config.ip;
    document.getElementById('settingsPort').value = config.port;
    document.getElementById('settingsKey').value = config.key;
    // Открываем окно
    document.getElementById('settingsModal').style.display = 'flex';
  }

  function closeSettings() {
    document.getElementById('settingsModal').style.display = 'none';
  }

  // Обновление статусов (пример)
  updateServerStatus(1, true);
  updateServerStatus(2, false);
  updateServerStatus(3, false);