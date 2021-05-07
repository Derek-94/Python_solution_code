function correctBrace(s) {
    let tmp = "";
    for(let i = 0 ; i < s.length ; i++) {
        if(tmp.length == 0) tmp += s[i];
        else if(tmp[tmp.length - 1] == "(" && s[i] == ")") {
            tmp = tmp.slice(0, tmp.length - 1);
        } else {
            tmp += s[i];
        }
    }
    return tmp.length === 0 ? true : false;
}

function minimumBalancedBrace(s) {
    let left = 0;
    let right = 0;
    for(let i = 0 ; i < s.length ; i++) {
        if(s[i] === "(") left += 1;
        else right += 1;
        if(left === right) {
            return s.slice(0, i + 1);
        }
    }
}

function opposite(s) {
    let returnStr = "";
    for(let i = 0 ; i < s.length ; i++) {
        if(s[i] == "(") {
            returnStr += ")";
        } else {
            returnStr += "(";
        }
    }
    return returnStr;
}

function recursive(s) {
    if(s.length === 0) return "";
    let u = minimumBalancedBrace(s);
    let v = s.slice(u.length)

    if(correctBrace(u) == true) {
        return u + solution(v);
    } else {
        let tmp = "";
        tmp += "(";
        tmp += solution(v);
        tmp += ")";
        let rmAfter = u.slice(1, u.length - 1);
        tmp += opposite(rmAfter);
        return tmp;
    }
}

function solution(p) {
    var answer = '';
    
    if(correctBrace(p) == true) return p;
    answer = recursive(p);

    return answer;
}