let timer = document.querySelector('.countdown');
let time = {mins: 20, secs: 0};

setInterval(() => {
    if (time.mins != 0) {
        if (time.secs == 0) {
            time.secs = 60;
            time.mins--;
        }
        time.secs--;
        timer.innerHTML = (time.secs.toString().length == 1) ? `${time.mins}:0${time.secs}` : `${time.mins}:${time.secs}`;
    }
}, 1000);

$('.option').hover(function () {
        $(this).css({'border-color': '#4481eb'});
        $(this).children('.opt-no').css({'background': '#4481eb', 'color': 'white'});
    }, function () {
        $(this).css({'border-color': '#f5f5f5'});
        $(this).children('.opt-no').css({'background': '#f5f5f5', 'color': 'black'});

    }
);

$('.option').click(function() {
    $(this).css({'border-color': '#4481eb'});
    $(this).children('.opt-no').css({'background': '#4481eb', 'color': 'white'});
});

const nav_que = document.querySelectorAll('.question');
let last_active = nav_que[0];

nav_que.forEach(function(btn) {
    btn.addEventListener('click', function() {
        last_active.classList.remove('active-que');
        btn.classList.add('active-que');
        last_active = btn;
        change_que_view(parseInt(btn.getAttribute('data-id')))
    });
});

const prev_btn = document.querySelector('#prev-btn');
const skip_btn = document.querySelector('#skip-btn');
const options = document.querySelectorAll('.option span');

function change_que_view(que_id) {
    $.ajax({
        type: "GET",
        url: `/dbcontent/questions/${que_id}/`,
        success: function (response) {
            $('.que-content p').text(response.que);
            $('.que-content span').text(`0${response.que_id}`);

            Object.entries(response.opts).forEach(([k, opt], i) => {
                options[i].innerHTML = opt;
            });
        }
    });
}

skip_btn.addEventListener('click', function() {
    let active = document.querySelector('.active-que');
    let active_no = parseInt(active.getAttribute('data-id'));

    if (active_no == 10) {
        skip_btn.disabled = true;
    } else {
        skip_btn.disabled = false;
        prev_btn.disabled = false;
        let nxt_que = document.querySelector(`.question[data-id="${active_no+1}"]`);
        active.classList.remove('active-que');
        nxt_que.classList.add('active-que');
        last_active = nxt_que;
        active_no++;
        change_que_view(active_no);
    }

});

prev_btn.addEventListener('click', function() {
    let active = document.querySelector('.active-que');
    let active_no = parseInt(active.getAttribute('data-id'));
    
    if (active_no == 1) {
        prev_btn.disabled = true;
    } else {
        prev_btn.disabled = false;
        skip_btn.disabled = false;
        let prev_que = document.querySelector(`.question[data-id="${active_no-1}"]`);
        active.classList.remove('active-que');
        prev_que.classList.add('active-que');
        last_active = prev_que;
        active_no--;
        change_que_view(active_no);
    }

});