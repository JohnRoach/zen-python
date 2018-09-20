Feature: Health check
  Our API should be able to provide a status on the
  health of the API to requesters

  Scenario: Happy Path
     Given Zen is set up
      When A request for the endpoint "/health"
      Then a 200 response with OK in the body is returned
