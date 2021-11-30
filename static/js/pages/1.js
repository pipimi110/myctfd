(function () {
    /*建立模态框对象*/
    // document.querySelectorAll('[id^="triggerBtn-"]');
    modalBoxes = []
    document.querySelectorAll('[id^="triggerBtn-"]').forEach(function (value, key) {
        // console.log(value) 
        var modalBox = {};
        /*获取模态框*/
        // modalBox.modal = document.getElementById("myModal-1");
        modalBox.modal = value.nextElementSibling;
        /*获得trigger按钮*/
        // modalBox.triggerBtn = document.getElementById("triggerBtn");
        // modalBox.triggerBtn = document.getElementById("triggerBtn-1");
        modalBox.triggerBtn = value;
        /*获得关闭按钮*/
        // modalBox.closeBtn = document.getElementById("closeBtn-1");
        modalBox.closeBtn = value.nextElementSibling.children[0].children[0].children[0];
        /*模态框显示*/
        modalBox.show = function () {
            console.log(this.modal);
            this.modal.style.display = "block";
        }
        /*模态框关闭*/
        modalBox.close = function () {
            this.modal.style.display = "none";
        }
        /*当用户点击模态框内容之外的区域，模态框也会关闭*/
        modalBox.outsideClick = function () {
            var modal = this.modal;
            window.onclick = function (event) {
                if (event.target == modal) {
                    modal.style.display = "none";
                }
            }
        }
        /*模态框初始化*/
        modalBox.init = function () {
            var that = this;
            this.triggerBtn.onclick = function () {
                that.show();
            }
            this.closeBtn.onclick = function () {
                that.close();
            }
            this.outsideClick();
        }
        modalBoxes.push(modalBox)
    })
    modalBoxes.forEach(function (value, key) {
        value.init();
    });

    function submit_flag(cid, flag) {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function () {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                console.log(xmlhttp.responseText);
            }
        }
        xmlhttp.open("POST", "/flag", true);
        xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xmlhttp.send(`cid=${cid}&flag=${flag}`);
    }
    
    var elements = document.getElementsByClassName("challenge-submit");
    for (var i = 0; i < elements.length; i++) {
        elements[i].onclick = function () {
            cid = this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement["id"].substring("myModel-".length);
            flag = this.parentElement.parentElement.firstElementChild.children[1].value;
            //console.log(cid);
            //console.log(flag);
            //console.log(123)//this.style.display="block";
            submit_flag(cid, flag);
        };
    }

})();

