var clientId = '219878077882-ukhuv0p0h332r4pg630tc7flehpqgcbi.apps.googleusercontent.com';
var apiKey = 'AIzaSyDhIvM2OzooWtDHN22cvyQgLTTbW-rkjsg';
var scopes = 'https://www.googleapis.com/auth/analytics.readonly';

function handleClientLoad () {
  gapi.client.setApiKey(apiKey);
  window.setTimeout(checkAuth, 1);
}

function checkAuth () {
  // Call the Google Accounts Service to determine the current user's auth status.
  // Pass the response to the handleAuthResult callback function
  gapi.auth.authorize({client_id: clientId, scope: scopes, immediate: true}, handleAuthResult);
}

function handleAuthResult (authResult) {
  if (authResult) {
    // The user has authorized access
    // Load the Analytics Client. This function is defined in the next section.
    loadAnalyticsClient();
  } else {
    // User has not Authenticated and Authorized
    handleUnAuthorized();
  }
}

// Authorized user
function handleAuthorized () {
  var status = document.querySelector('.js-ga-connect-status');
  if (status) {
    status.innerHTML = '<span class="fa fa-check-square"></span> Connected to Google Analytics';
  }
  queryAccounts();
}

// Unauthorized user
function handleUnAuthorized () {
  console.log('Unauthorized');
}

function loadAnalyticsClient () {
  // Load the Analytics client and set handleAuthorized as the callback function
  gapi.client.load('analytics', 'v3', handleAuthorized);
}


function queryAccounts () {
  console.log('Querying Accounts.');

  // Get a list of all Google Analytics accounts for this user
  gapi.client.analytics.management.accounts.list().execute(handleAccounts);
}

function handleAccounts (results) {

  if (!results.code) {
    if (results && results.items && results.items.length) {

      $.each(results.items, function(idx, val) {
        queryWebproperties(val.id);
      });

    } else {
      console.log('No accounts found for this user.')
    }
  } else {
    console.log('There was an error querying accounts: ' + results.message);
  }
}

function queryWebproperties (accountId) {
  console.log('Querying Webproperties.');

  // Get a list of all the Web Properties for the account
  gapi.client.analytics.management.webproperties.list({'accountId': accountId}).execute(handleWebproperties);
}

function handleWebproperties (results) {
  if (!results.code) {
    if (results && results.items && results.items.length) {

      $.each(results.items, function(idx, val) {
        queryProfiles(val.accountId, val.id);
      });

    } else {
      console.log('No webproperties found for this user.');
    }
  } else {
    console.log('There was an error querying webproperties: ' + results.message);
  }
}

function queryProfiles (accountId, webpropertyId) {
  console.log('Querying Views (Profiles).');

  // Get a list of all Views (Profiles) for the first Web Property of the first Account
  gapi.client.analytics.management.profiles.list({
    'accountId': accountId,
    'webPropertyId': webpropertyId
  }).execute(handleProfiles);
}

function handleProfiles (results) {
  if (!results.code) {
    if (results && results.items && results.items.length) {

      renderViews(results);


      // Get the first View (Profile) ID
      //var firstProfileId = results.items[0].id;

      // Step 3. Query the Core Reporting API
      //queryCoreReportingApi(firstProfileId);

    } else {
      console.log('No views (profiles) found for this user.');
    }
  } else {
    console.log('There was an error querying views (profiles): ' + results.message);
  }
}

function renderViews (results) {
  var $views = $('.js-views');

    $.get('/views').done(function(html) {
        Mustache.parse(html);
        $.each(results.items, function(idx, item) {
            var $item = $(Mustache.render(html, item));
            $views.append($item);

            $item.on('click', function () {
                getGoals({
                  accountId: item.accountId,
                  webPropertyId: item.webPropertyId,
                  id: item.id
                });
            });
      });
    });
}

function template (id, results) {
  return $.get('/' + id).pipe(function(html) {
    Mustache.parse(html);
    return Mustache.render(html, results);
  });
}

function getGoals (view) {
  var request = gapi.client.analytics.management.goals.list({
    'accountId': view.accountId,
    'webPropertyId': view.webPropertyId,
    'profileId': view.id
  });
  request.execute(renderGoals);
}

function renderGoals (results) {
  var goals = document.querySelector('.js-goals');

  if (results.items && results.items.length) {
    template('goals', results).done(function(html) {
      goals.innerHTML = html;
    });
  } else {
    goals.innerHTML = '<p>No goals available for the view you have selected.</p>';
  }

}

//function queryCoreReportingApi(profileId) {
//  console.log('Querying Core Reporting API.');
//
//  // Use the Analytics Service Object to query the Core Reporting API
//  gapi.client.analytics.data.ga.get({
//    'ids': 'ga:' + profileId,
//    'start-date': '2012-03-03',
//    'end-date': '2012-03-03',
//    'metrics': 'ga:sessions'
//  }).execute(handleCoreReportingResults);
//}
//
//function handleCoreReportingResults(results) {
//  if (results.error) {
//    console.log('There was an error querying core reporting API: ' + results.message);
//  } else {
//    printResults(results);
//  }
//}
//
//function printResults(results) {
//  if (results.rows && results.rows.length) {
//    console.log('View (Profile) Name: ', results.profileInfo.profileName);
//    console.log('Total Sessions: ', results.rows[0][0]);
//  } else {
//    console.log('No results found');
//  }
//}

document.querySelector('.js-connect-ga').addEventListener('click', function (evt) {
  gapi.auth.authorize({client_id: clientId, scope: scopes, immediate: false}, handleAuthResult);
  $('.js-views-container').removeClass('hidden');
  $('.js-help').addClass('hidden');
  return false;
});