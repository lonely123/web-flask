var log=function () {
    console.log.apply(console,arguments)
}
var e = function(sel) {
    return document.querySelector(sel)
}
// var loginTemplate = function (login) {
//     var t =`<div>
//             <h3>${login}</h3>
//             </div>
//             `
//     return t
// }

var a=e('.login-form')
var d=e('#login')
var u=e('#username')
var s=e('.stats')
d.addEventListener('click',function() {
    log('click')
    user=u.value
    if(user.length>2){
            log('检查合格')
            s.innerHTML='检查合格'
            // a.insertAdjacentHTML('beforeend',loginTemplate('检查合格'))
    }
    else {
            log('用户名错误')
            u.value=''
            s.innerHTML='用户名错误'
            // a.insertAdjacentHTML('beforeend',loginTemplate('用户名错误'))
    }

})


