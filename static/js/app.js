(function() {
	angular.module('bias', []);
	angular.module('bias')
	.component('biasWrapper',{
		templateUrl: '/static/biasWrapper.html',
		controller: BiasWrapperCtrl
	})
	.component('biasResult', {
			templateUrl: '/static/biasResult.html',
			bindings: {
				onReset: '&',
				result: '<'
			}
	})
	.component('biasForm', {
		templateUrl: '/static/biasFrom.html',
		bindings: {
			text: '=',
			code: '=',
			onSubmit: '&'
		}
	});



	function BiasWrapperCtrl ($http) {
		var ctrl = this;

		ctrl,$onInit = function () {
			ctrl.text = '';
			ctrl.code = '';
			ctrl.resultFetched = false;
			ctrl.result = null;
			ctrl.isChecking = false;
		}

		ctrl.checkText = function () {
			ctrl.isChecking = true;
				$http.post('api/text/estimate', {code: this.code, text: this.text})
				.then(function(payload) {
					ctrl.resultFetched = true;
					ctrl.result = payload.data;
				}, function(err) {
						 Materialize.toast(' <i class="material-icons">warning</i>Your code in incorrect!', 4000)
				})
				.finally(function() {
						ctrl.isChecking = false;
				})
		}

		ctrl.reset = function () {
			ctrl.resultFetched = false;
			ctrl.text = '';
			ctrl.code = '';
		}
	}
})();