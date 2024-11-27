These images were used to generate IAC using Chatgpt-4. They followed a specific prompt as follows:

"Can you create IAC code for the attached image?
Define Service Types and Containerization Requirements.
Use Docker and Kubernetes.
Big Services: For large services that need their own dedicated resources, set them up in individual containers. Examples include major backend services or databases that demand isolation.
Microservices: Group smaller, related microservices in shared containers where feasible or use Kubernetes pods for related services that need to be orchestrated together."

Refined docker-compose prompt as follows:

"Can you generate a Docker Compose YAML file for the attached design image? 
Ensure the following:
1. Service Definitions:
	Define all services based on the design. Each service should run in its own container.
2. Resource Allocation:
	Allocate memory and CPU for services individually using deploy.resources.
3. Networking:
	Use a single shared network to allow communication between all services and add ports.
4. Service Isolation:
	Deploy services in their own containers with dedicated resources where necessary.
5. Include comments for each section to explain your implementation choices."