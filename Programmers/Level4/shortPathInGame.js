let dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
let candidate = [];

function DFS(visited, que, maps) {
    let [curX, curY] = que.pop();
    for(let i = 0 ; i < dirs.length ; i++) {
        let [nX, nY] = [curX + dirs[i][0], curY + dirs[i][1]];
        if(nX >= 0 && nX < maps.length && nY >= 0 && nY < maps[0].length) {
            if(maps[nX][nY] === 1 && visited[nX][nY] === 0) {
                que.push([nX, nY]);
                visited[nX][nY] = 1;
                cnt += 1;
                console.log(`${nX}, ${nY} 방문함. cnt 값은 ${cnt}`)
                if(nX === maps.length - 1 && nY === maps[0].length - 1) {
                    console.log(`마침.  cnt 값은 ${cnt}`)
                    candidate.push(cnt);
                    visited[nX][nY] = 0;
                    return;
                }
                dfs(visited, que, maps);
                cnt -= 1;
                console.log(`${nX}, ${nY} 해제. cnt 값은 ${cnt}`)
                
                visited[nX][nY] = 0;
            }
        }
    }    
}

function BFS(visited, que, maps) {
    while(que.length > 0){
        let curX = que[0][0];
        let curY = que[0][1];
        let curCnt = que[0][2];
        que.shift();
        if(curX === maps.length - 1 && curY === maps[0].length - 1) {
            return curCnt;
            break;
        }
        for(let i = 0 ; i < dirs.length ; i++) {
            let [nX, nY] = [curX + dirs[i][0], curY + dirs[i][1]];
            if(nX >= 0 && nX < maps.length && nY >= 0 && nY < maps[0].length) {
                if(maps[nX][nY] === 1 && visited[nX][nY] === 0) {
                    que.push([nX, nY, curCnt + 1]);
                    visited[nX][nY] = 1;
                    // console.log(`${nX}, ${nY} 방문했다, cnt는 ${curCnt}`)
                }
            }
        }
    }
}

function solution(maps) {
    var answer = 0;
    
    let que = [];
    
    let visited = new Array(maps.length);
    for(let i = 0 ; i < maps.length ; i++) {
        visited[i] = new Array(maps[0].length);
    }
    for(let i = 0 ; i < maps.length ; i++) {
        for(let j = 0 ; j < maps[0].length ; j ++) {
            visited[i][j] = 0;
        }
    }
    
    que.push([0, 0, 1]);
    visited[0][0] = 1;
    // DFS(visited, que, maps)
    answer = BFS(visited, que, maps);
            
    return typeof(answer) === "number" ? answer : -1
}