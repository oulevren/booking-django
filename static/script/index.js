sliderNum1()

function sliderNum1() {



    const sliderBox = document.querySelector(".slider_elements");
    const buttonLeft = document.querySelector(".slider_left");
    const buttonRight = document.querySelector(".slider_right");
    let count = 0

    buttonRight.addEventListener('click', () => {

        if (count < 7) {
            buttonRight.classList.remove('none');
            buttonLeft.classList.remove('none');
            count++
            if (count == 7) {
                buttonRight.classList.add('none');
            }

        } else {
            buttonRight.classList.remove('none');
            count = count
        }
        sliderBox.style.left = `${"-" + (count * 225)}px`;

    });

    buttonLeft.addEventListener('click', () => {

        if (count > 0) {
            buttonLeft.classList.remove('none');
            buttonRight.classList.remove('none');
            count--
            if (count == 0) {
                buttonLeft.classList.add('none');
            }
        } else {
            buttonLeft.classList.remove('none');
            count = count
        }
        sliderBox.style.left = `${"-" + (count * 225)}px`;

    });

}


//  MERT

sliderNum3()

function sliderNum3() {

    const sliderBox3 = document.querySelector(".slider5_elements");
    const buttonLeft3 = document.querySelector(".slider_left_3");
    const buttonRight3 = document.querySelector(".slider_right_3");
    let count3 = 0

    buttonRight3.addEventListener('click', () => {

        if (count3 < 4) {
            buttonRight3.classList.remove('none');
            buttonLeft3.classList.remove('none');
            count3++
            if (count3 == 4) {
                buttonRight3.classList.add('none');
            }

        } else {
            buttonRight3.classList.remove('none');
            count3 = count3
        }

        sliderBox3.style.left = `${"-" + (count3 * 281.5)}px`;
    });

    buttonLeft3.addEventListener('click', () => {

        if (count3 > 0) {
            buttonLeft3.classList.remove('none');
            buttonRight3.classList.remove('none');
            count3--
            if (count3 == 0) {
                buttonLeft3.classList.add('none');
            }
        } else {
            buttonLeft3.classList.remove('none');
            count3 = count3
        }

        sliderBox3.style.left = `${"-" + (count3 * 281.5)}px`;

    });

}



let btns = document.querySelectorAll('#btn, #btn2, #btn3, #btn4, #btn5, #btn6');

btns.forEach(function (button) {
    let isButtonStyled = false; // Her düğme için ayrı bir stil durumu

    button.addEventListener('click', function onClick() {
        if (!isButtonStyled) {
            // Düğmenin yeni stilini ayarla
            button.style.backgroundColor = 'lightblue';
            button.style.color = 'blue';
            button.style.border = '1px solid blue';
            isButtonStyled = true; 
        } else {
            // Düğmenin stilini eski haline getir
            button.style.backgroundColor = '';
            button.style.color = '';
            button.style.border = '';
            isButtonStyled = false; 
        }
    });
});

//Emine

//* 2 farklı swiper olduğu için farklı class name ler tanımlayıp querySelector ile ilgili class a ulaşılıp yapı oluşturuldu
const swiperEl = document.querySelector(".swiper-1");
Object.assign(swiperEl, {
  slidesPerView: 1, //* kaç tane slaytın aynı anda görünmesini istediğimiz
  navigation: true, //* swiper yapısı içinde gezmek true mu false mu olsun
  breakpoints: {   //* ekran genişliğine göre slidesPerView ü ayarrlıyoruz
    640: {
      slidesPerView: 2,
      spaceBetween: 5,
    },
    768: {
      slidesPerView: 3,
      spaceBetween: 5,
    },
    1024: {
      slidesPerView: 4,
      spaceBetween: 5,
    },
  },
});
swiperEl.initialize();


const swiperEl2 = document.querySelector(".swiper-2");
Object.assign(swiperEl2, {
  slidesPerView: 1,
  navigation: true,
  breakpoints: {
    640: {
      slidesPerView: 2,
      spaceBetween: 5,
    },
    768: {
      slidesPerView: 3,
      spaceBetween: 5,
    },
    1024: {
      slidesPerView: 4,
      spaceBetween: 5,
    },
  },
});
swiperEl2.initialize();

//Emine Bitiş



// Detay1 dropdown

function toggleDropdown() {
    var dropdown = document.getElementById("dropdown-menu");
    if (dropdown.style.display === "block") {
      dropdown.style.display = "none";
    } else {
      dropdown.style.display = "block";
    }
  }
  
  var dropdownItems = document.querySelectorAll("#dropdown-menu a");
  
  dropdownItems.forEach(function(item) {
    item.addEventListener("click", function(e) {
      e.preventDefault();
      var buttonText = item.textContent;
      var button = document.querySelector(".input-popular button");
      button.textContent = "Sırala: " + buttonText;
      toggleDropdown();
    });
  });

// Deniz Başlangıç
//! Sıradaki seyahatlar kısmındaki değişen yazının javascripti 
const textArray = [
  "eviniz",
  "kulübeler",
  "daireler",
  "apart oteller",
  "villalar",
  "tatil evleri"
  ];
  let currentIndex = 0;
  const textElement = document.getElementById("text-container");

  function changeText() {
  textElement.innerHTML = textArray[currentIndex];
  currentIndex = (currentIndex + 1) % textArray.length;
  }

  setInterval(changeText, 1000);


//! Beğendiğimiz seyahat noktaları JAVASCRİPT Kısmı

function openBOLGELER() {
  document.getElementById('content-1').style.display = 'block';
  document.getElementById('content-2').style.display = 'none';
  document.getElementById('content-3').style.display = 'none';
}

function openSEHIRLER() {
  document.getElementById('content-1').style.display = 'none';
  document.getElementById('content-2').style.display = 'block';
  document.getElementById('content-3').style.display = 'none';
}

function openSIMGESELYAPILAR() {
  document.getElementById('content-1').style.display = 'none';
  document.getElementById('content-2').style.display = 'none';
  document.getElementById('content-3').style.display = 'block';
}


// Deniz Bitiş






