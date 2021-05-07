function checkBrace(s) {
    let checkString = "";
    let smallFlag = false;
    let midFlag = false;
    let bigFlag = false;
    for(let i = 0 ; i < s.length ; i++) {
        if(smallFlag === false && s[i] == ")") {
            return false;
        } else if(smallFlag === false && s[i] == "(") {
            checkString += "(";
            smallFlag = true;
        } else if(smallFlag === true && s[i] == "(") {
            checkString += "(";
            smallFlag = true;
        } else if(smallFlag === true && s[i] == ")" && checkString[checkString.length - 1] == "(") {
            checkString = checkString.slice(0, checkString.length - 1);
        } else if(midFlag === false && s[i] == "}") {
            return false;
        } else if(midFlag === false && s[i] == "{") {
            checkString += "{";
            midFlag = true;
        } else if(midFlag === true && s[i] == "{") {
            checkString += "{";
            midFlag = true;
        } else if(midFlag === true && s[i] == "}" && checkString[checkString.length - 1] == "{") {
            checkString = checkString.slice(0, checkString.length - 1);
        } else if(bigFlag === false && s[i] == "]") {
            return false;
        } else if(bigFlag === false && s[i] == "[") {
            checkString += "[";
            bigFlag = true;
        } else if(bigFlag === true && s[i] == "[") {
            checkString += "[";
            bigFlag = true;
        } else if(bigFlag === true && s[i] == "]" && checkString[checkString.length - 1] == "[") {
            checkString = checkString.slice(0, checkString.length - 1);
        }
    }
    return checkString.length == 0 ? true : false;
}

function solution(s) {
    let answer = 0;
    let modifiedS = "";
    
    for(let i = 0 ; i < s.length ; i++) {
        modifiedS = s.slice(i)  + s.slice(0, i);
        if(checkBrace(modifiedS) == true) answer += 1;
    }
    
    return answer;
}