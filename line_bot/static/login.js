document.addEventListener('DOMContentLoaded', function() {
    var closeButton = document.getElementById('myButton');
    var countdown = 10;
  
    closeButton.addEventListener('click', function() {
      closeWindow();
    });
    function closeWindow() {
      window.open('',"_self")
      window.close();
    }
  
    function startCountdown() {
      closeButton.innerText = countdown + '秒後將會自動確認並關閉，或點擊此按鈕立即關閉';
      countdown--;
        
      if (countdown < 0) {
        window.open('',"_self")
        closeWindow();
      } else {
        setTimeout(startCountdown, 1000);
      }
    }
  
    setTimeout(startCountdown, 0);
  });