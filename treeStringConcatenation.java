import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Iterator;

class Node {
		
		String data;
		Deque<Node> children = new ArrayDeque<>();
		
		Node(String data) {
			this.data = data; 
		}		
	}
	
	class Tree {
		Node root;
		Tree(Node root) {
			this.root = root;
		}
	}
	
	class Solution {
		
		Tree tree;
		
		Solution(int t, int type) {
			Node html = new Node("<html>");
			Node H = new Node("H");
			Node ello = new Node("ello");
			if (t == 1) {
				// Build tree1
				tree = new Tree(html);
				Node head = new Node("<head>");
				Node body = new Node("<body>");
				html.children.add(head);
				html.children.add(body);
				Node title = new Node("<title>");
				head.children.add(title);
				Node my = new Node("my ");
				Node awesome = new Node("awesome ");
				Node website = new Node("website");
				title.children.add(my);
				title.children.add(awesome);
				title.children.add(website);
				Node div = new Node("<div>");
				body.children.add(div);
				Node p = new Node("<p>");
				p.children.add(p);				
			} else if (t == 2) {
				//Build tree2
				tree = new Tree(html);
				Node p1 = new Node("<p>");
				Node p2 = new Node("<p>");
				html.children.add(p1);
				p1.children.add(p2);
				p1.children.add(H);
				Node p3 = new Node("<p>");
				html.children.add(p3);
				p3.children.add(ello);
			}
			if (type == 1) {
			    recursiveSolution(html);
			} else if (type == 2) {
				iterativeSolution(html);
			} else {
				bradySolution(html);
			}
		}
		/* dsfsdfs */
		
		void bradySolution(Node root) {
			
			
		}
		
		public void recursiveSolution(Node n) {
			if (n == null) {
				return;				
			}
			if (n.children.isEmpty()) {
			    if (	n.data.charAt(0) != '<') {
			    		System.out.print(n.data);
			    }
			    return;
			}
			for (Node child: n.children) {
				recursiveSolution(child);				
			}
		}
		
		public void iterativeSolution (Node n) {
			Deque<Node> stack = new ArrayDeque<Node>();
			stack.push(n);
			while (!stack.isEmpty()) {
				Node curr = stack.pop();
				//System.out.println(curr.data);
				if (curr.children.isEmpty()) {
					if (curr.data.charAt(0) != '<') {
						System.out.print(curr.data);
					}
				} else {
					Iterator<Node> iterator = curr.children.descendingIterator();
					while (iterator.hasNext()) {
						Node next = iterator.next();
						//System.out.println(next.data);
						stack.push(next);
					}
				}
			}
		}
		
	}


public class main {
	public static void main(String[] args) {
//		Solution sol1 = new Solution(1);
		Solution sol2 = new Solution(1, 2);
		
		
       
		
		
		
//		String str = "Hello my name is Jennifer";
//		int H = 2;
//		int L = 20;
//		int times = 0;
//		
//		int len = str.length();
//		int leftover = 0;
//		for (int i = 0; i<H; i++) {
//			times += (L - leftover)/(len + 1);
//			if (L - leftover >= 0) {
//				times += 1;
//			}
//			leftover = L % len;
//		}
//		// final space
//		// split on word vs space
//		// runs over 2 lines 
//		System.out.println(times);
	}

}
