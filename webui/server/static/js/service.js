app.factory("HttpService", function($http) {

	return {
		get: function(path, params, successCallBack, failureCallBack) {
			params = params || {};

			$http({
				method: 'GET',
				url: path,
				params: params,
				headers: {
					'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
				}
			}).then(function(response) {
				successCallBack(response);
			}, function(error) {
				failureCallBack(error);
			});
		},
		post: function(path, params, successCallBack, failureCallBack) {
			params = params || {};

			$http({
				method: 'POST',
				url: path,
				data: $.param(params),
				headers: {
					'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
				}
			}).then(function(response) {
				successCallBack(response);
			}, function(error) {
				failureCallBack(error);
			});
		},
		put: function(path, params, successCallBack, failureCallBack) {
			params = params || {};

			$http({
				method: 'PUT',
				url: path,
				data: $.param(params),
				headers: {
					'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
				}
			}).then(function(response) {
				successCallBack(response);
			}, function(error) {
				failureCallBack(error);
			});
		},
		delete: function(path, params, successCallBack, failureCallBack) {
			params = params || {};
			$http({
				method: 'DELETE',
				url: path,
				data: $.param(params),
				headers: {
					'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
				}
			}).then(function(response) {
				successCallBack(response);
			}, function(error) {
				failureCallBack(error);
			});
		}
	}

});