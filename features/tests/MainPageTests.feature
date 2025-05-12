# Created by jraiv at 4/22/2025
Feature: Test Cases

  @smoke
  Scenario: User can filter the Secondary deals by Unit price range
    Given Open Reely main page
    When Enter email and password
    And Click continue
    And Click 'Secondary' option
    And Verify the page opens
    And Click on 'filters' button
    And Apply price range filters
    And Click 'Apply Filter'
#    Then Verify the price is in correct range
