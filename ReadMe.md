# NLP Server for Remote Applications

A server for running NLP tasks outside of a program. Allows for models to stay
loaded. Based on http so it can be load balanced.

## Use cases

Uses cases include:

- Calling NLP functions from Pentaho
- Reducing load times for projects requiring model data
- NLP tasks in production

## Requirements

This project uses Celery to run processes asynchronously. Asyncio forms the bases of the http
server.

The requirements include:
- celery
- aiohttp

## Starting the Appliation and Server

Since processing runs in celery, you need to start celery first and then the http server.

## License

Copyright 2019- Andrew S Evans

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.