These images were used to generate IAC using Chatgpt-4. They followed a specific prompt as follows:

"Can you create IAC code for the attached image?
Define Service Types and Containerization Requirements.
Use Docker and Kubernetes.
Big Services: For large services that need their own dedicated resources, set them up in individual containers. Examples include major backend services or databases that demand isolation.
Microservices: Group smaller, related microservices in shared containers where feasible or use Kubernetes pods for related services that need to be orchestrated together."

Refined docker-compose prompt as follows:

"Can you generate a Docker Compose YAML file for the attached design image?
Please ensure the following:

1.Service Definitions:
	Define all services based on the design image.
	Each service should run in its own container.
2.Resource Allocation:
	Allocate memory and CPU limits for each service using deploy.resources.
3.Service Connections:
	Configure container-to-container communication appropriately.
	Use service names as hostnames to enable networking and add ports.
4.Service Isolation:
	Deploy each service in its own container, ensuring dedicated resources are used when necessary.
5.Documentation:
	Include clear and descriptive comments for each section to explain your implementation choices"