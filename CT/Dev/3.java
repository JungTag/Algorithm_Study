import java.util.ArrayList;

class Solution {
    int cnt = 0;

    public int solution(int n, int[][] wires) {
        int answer = 101;

        for(int i=0; i<wires.length; i++) {
            ArrayList<int[]> newWires = new ArrayList<int[]>();
            for(int j=0; j<wires.length; j++) {
                if (j != i) {
                    newWires.add(wires[j]);
                }
            }

            // 그래프 초기화
            ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();
            for(int k=0; k<n+1; k++) {
                graph.add(new ArrayList<Integer>());
            }
            for(int[] pair:newWires) {
                int v1 = pair[0];
                int v2 = pair[1];
                graph.get(v1).add(v2);
                graph.get(v2).add(v1);
            }

            boolean[] visited = new boolean[n+1];
            for(int l=0; l<n+1; l++) {
                visited[l] = false;
            }

            // 그래프 탐색
            ArrayList<Integer> result = new ArrayList<Integer>();
            for(int v=1; v<n+1; v++) {
                if(visited[v] == false) {
                    result.add(dfs(v, visited, graph));
                    cnt = 0;
                }
            }

            int diff = Math.abs(result.get(0) - result.get(1));
            result.clear();
            if (answer > diff) {
                answer = diff;
            }
        }
        return answer;
    }

    public int dfs(int node, boolean[] visited, ArrayList<ArrayList<Integer>> graph) {
        visited[node] = true;
        cnt += 1;
        
        for(int adj:graph.get(node)) {
            if (visited[adj] == false) {
                dfs(adj, visited, graph);
            }
        }
        return cnt;
    }
}