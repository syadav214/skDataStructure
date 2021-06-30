import java.util.HashMap;

class djikstra {
    static HashMap<String, Boolean> processed = new HashMap<>();

    public static void main(String[] arg){

        HashMap<String,HashMap> graph = new HashMap<>();

        HashMap<String,Integer> startNeighbours = new HashMap<>();
        startNeighbours.put("A",6);
        startNeighbours.put("B",2);
        graph.put("Start", startNeighbours);

        HashMap<String,Integer> ANeighbours = new HashMap<>();
        ANeighbours.put("Fin",1);
        graph.put("A", ANeighbours);

        HashMap<String,Integer> BNeighbours = new HashMap<>();
        BNeighbours.put("A",3);
        BNeighbours.put("Fin",5);
        graph.put("B", BNeighbours);

        graph.put("Fin", new HashMap<>());


        HashMap<String,Integer> costs = new HashMap<>();
        costs.put("A",6);
        costs.put("B",2);
        costs.put("Fin",Integer.MAX_VALUE);

        HashMap<String,String> parents = new HashMap<>();
        parents.put("A","Start");
        parents.put("B","Start");
        parents.put("Fin","None");

        String node =  find_lowest_cost_node(costs);
        while(node != ""){
            int cost = costs.get(node);
            HashMap<String,Integer> neighbours = graph.get(node);
            for(String n: neighbours.keySet()){
                int newCost = cost + neighbours.get(n);
                if(costs.get(n) > newCost){
                    costs.put(n, newCost);
                    parents.put(n,node);
                }
            }
            processed.put(node, true);
            node = find_lowest_cost_node(costs);
        }

    }

    static String find_lowest_cost_node(HashMap<String,Integer> costs){
        int low = Integer.MAX_VALUE;
        String lowNode ="";
        for(String a: costs.keySet()){
            if(costs.get(a) < low && Boolean.FALSE.equals(processed.containsKey(a))){
                low = costs.get(a);
                lowNode = a;
            }
        }
        return  lowNode;
    }

}