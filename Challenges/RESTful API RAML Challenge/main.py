
doc = '''
#%RAML 1.0
title: RESTful API RAML Challenge
version: 1.0.0
protocols: [HTTPS]
securitySchemes:
  JWT:
    description: Authentication with JWT
    type: JWT
    settings:
      signatures: ['HMAC-SHA256']
    describedBy:
      headers:
        Authorization:
          type: string
      responses:
        401: "Authentication problem (JWT not set or expired)"
types:
  Auth:
    type: object
    discriminator: token
    properties:
      token : string
  Event:
    type: object
    discriminator: event
    description: Model for the Event Table
    properties:
      event_id:
        required: true
        type: integer
      agent_id:
        type: integer
      level:
        type: string
      payload:
        type: string
      shelve:
        type: boolean
      date:
        type: datetime
    example:
      {
        event_id: 1,
        agent_id: 2,
        level: 'critical',
        payload: '000000000000',
        shelve: True,
        date: '0000-00-00T00:00:00:00Z',
      }
  Agent:
    type: object
    discriminator: agent
    description: Model for the Agent Table
    properties:
      agent_id:
        type: integer
      user_id:
        type: integer
      name:
        type: string
      status:
        type: boolean
      environment:
        type: string
      version:
        type: string
      address:
        type: string
    example:
      {
        agent_id: 1,
        user_id: 2,
        name: 'agent-name',
        status: True,
        environment: 'agent-environment',
        version: 'agent-version',
        address: 'agent-address',
      }
  Group:
    type: object
    discriminator: group
    description: Model for the Group Table
    properties:
      group_id:
        type: integer
      name:
        type: string
    example:
      {
        group_id: 1,
        name: 'group-name',
      }
  User:
    type: object
    discriminator: user
    description: Model for the User Table
    properties:
      user_id:
        type: integer
      name:
        type: string
      password:
        type: string
      email:
        type: string
      last_login:
        type: datetime
      group_id:
        type: integer
/auth/token:
  post:
    description: Request for recovering the JWT token
    body:
      application/json:
        username:
          type: string
        password:
          type: string
    tags: 
    - "Token"
    responses:
      201:
        body: "Success"
      400:
        body: "Denied"
/agents:
  post:
    description: Create Agent
    securedBy: [JWT]
    body:
      application/json:
        properties:
          type: Agent
          example:
            {
              agent_id: 1,
              name: "teste",
              status: true,
              environment: "abcdef",
              version: "1",
              address: "0.0.0.0",
              user_id: 1,
            }
    responses:
      201:
        body: Agent
      400:
        body: "Bad request"
      401:
        body: "Unauthorized"
  get:
    description: Get all the Agents
    securedBy: [JWT]
    tags:
    - "Agent"
    responses:
      200:
        body: Agent[]
      401:
        body: "Unauthorized"
  /{id}:
    get:
      description: Get a specific Agent by id
      securedBy: [JWT]
      tags:
      - "Agent"
      responses:
        200:
          body: Agent
        401:
          body: "Unauthorized"
        404:
          body: "Not Found"
    put:
      description: Update a specific Agent by id
      securedBy: [JWT]
      body:
        application/json:
          properties:
            type: Agent
      responses:
        200:
          body: "Success"
        401:
          body: "Unauthorized"
        404:
          body: "Not Found"
    delete:
      description: Delete a specific Agent by id
      securedBy: [JWT]
      responses:
        200:
          body: "Success"
        401:
          body: "Unauthorized"
        404:
          body: "Not Found"
  /{id}/events:
    post:
      description: Create Event related to agent
      securedBy: [JWT]
      body:
        application/json:
          properties:
            type: Event
      responses:
        201:
          body: "Created"
        400:
          body: "Bad request"
        401:
          body: "Unauthorized"
    get:
      description: Get all the Events related to agent
      securedBy: [JWT]
      tags:
      - "Event"
      responses:
        200:
          body: Event[]
        400:
          body: "Bad request"
        401:
          body: "Unauthorized"
    put:
      description: Update all the Events related to agent
      securedBy: [JWT]
      body:
        application/json:
          properties:
              type: Event
      tags:
      - "Event"
      responses:
        200:
          body: "Success"
        401:
          body: "Unauthorized"
        404:
          body: "Not Found"
    delete:
      description: Delete all the Events related to agent
      securedBy: [JWT]
      tags:
      - "Event"
      responses:
        200:
          body: "Success"
        401:
          body: "Unauthorized"
        404:
          body: "Not Found"
/groups:
  post:
    description: Create Group
    securedBy: [JWT]
    body:
      application/json:
        properties:
          type: Group
    responses:
      201:
        body: "Created"
      400:
        body: "Bad request"
      401:
        body: "Unauthorized"
  get:
    description: Get all the Groups
    securedBy: [JWT]
    tags:
    - "Group"
    responses:
      200:
        body: Group[]
      401:
        body: "Unauthorized"  
  /{id}:
    get:
      description: Get a specific Group by id
      securedBy: [JWT]
      tags:
      - "Group"
      responses:
        200:
          body: Group
        401:
          body: "Unauthorized"
        404:
          body: "Not Found"
    put:
      description: Update specific Group by id
      securedBy: [JWT]
      body:
        application/json:
          properties:
            type: Group
      tags:
      - "Group"
      responses:
        200:
          body: "Success"
        401:
          body: "Unauthorized"
        404:
          body: "Not Found"
    delete:
      description: Get specific Group by id
      securedBy: [JWT]
      tags:
      - "Group"
      responses:
        200:
          body: "Success"
        401:
          body: "Unauthorized"
        404:
          body: "Not Found"
/users:
  post:
    description: Create User
    securedBy: [JWT]
    body:
      application/json:
        properties:
          type: User
    tags:
    - "User"
    responses:
      201:
        body: "Created"
      400:
        body: "Bad request"
      401:
        body: "Unauthorized"
  get:
    description: Get all the Users
    securedBy: [JWT]
    tags:
    - "User"
    responses:
      200:
        body: User[]
      401:
        body: "Unauthorized"  
  /{id}:
    get:
      description: Get a specific User by id
      securedBy: [JWT]
      tags:
      - "User"
      responses:
        200:
          body: User
        401:
          body: "Unauthorized"
        404:
          body: "Not Found"
    put:
      description: Update a specific User by id
      securedBy: [JWT]
      body:
        application/json:
          properties:
            type: User
      tags:
      - "User"
      responses:
        200:
          body: "Success"
        401:
          body: "Unauthorized"
        404:
          body: "Not Found"
    delete:
      description: Delete a specific User by id
      securedBy: [JWT]
      tags:
      - "User"
      responses:
        200:
          body: "Success"
        401:
          body: "Unauthorized"
        404:
          body: "Not Found"
'''
