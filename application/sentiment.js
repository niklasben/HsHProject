var twitter = angular.module('myApp', ['ui.bootstrap','nvd3ChartDirectives']);

twitter.controller('myController', function($rootScope, $scope){
	$scope.view = "";
	$scope.selectView = function(view){
		console.log(view);
		$scope.view = view;
		if(view == ''){
			$scope.selectedData = {
				topic: "",
				country: "",
				values: ""
			};
		}
		if(view == 'countries'){
			if($scope.selectedData.country){
				$scope.selectedData = {
					topic: "",
					country: "",
					values: ""
				};
			}
			$scope.showCountries();
		}
		if(view == 'topics'){
			if($scope.selectedData.topic){
				$scope.selectedData = {
					topic: "",
					country: "",
					values: ""
				};
			}
			$scope.showTopics();
			
		}
	}
	$scope.topics = [];
	$scope.countries = [];
	$scope.selectedData = {
		topic: "",
		country: "",
		values: ""
	};
	$scope.showTopics = function(){
		if(!$scope.topics.length){
			angular.forEach($scope.data, function(value, key){
				console.log(value.value);
				$scope.topics.push(value.value);
			});
		}
	};
	$scope.selectTopic = function(index){
		$scope.selectedData.topic = {
			value: $scope.data[index].value,
			index: index
		}
		if($scope.selectedData.country){
			var cindex = $scope.selectedData.country.index;
			$scope.selectedData.values = $scope.data[index].content[cindex].rates;
			$scope.graphData = [
				{
					key: "Series 1",
					values: [[ "positive", $scope.selectedData.values.positive ],[ "neutral", $scope.selectedData.values.neutral ],[ "negative", $scope.selectedData.values.negative ]]
				}
			]
		}else{
			$scope.selectView('countries');
		}
	}
	$scope.showCountries = function(){
		if(!$scope.countries.length){
			angular.forEach($scope.data[0].content, function(c){
				$scope.countries.push(c.value);
			});
		}
	};
	$scope.selectCountry = function(index){
		$scope.selectedData.country = {
			value: $scope.data[0].content[index].value,
			index: index
		}
		if($scope.selectedData.topic){
			var tindex = $scope.selectedData.topic.index;
			$scope.selectedData.values = $scope.data[tindex].content[index].rates;
			console.log($scope.selectedData.values.positive);
			$scope.graphData = [
				{
					key: "Series 1",
					values: [[ "positive", $scope.selectedData.values.positive ],[ "neutral", $scope.selectedData.values.neutral ],[ "negative", $scope.selectedData.values.negative ]]
				}
			]
		}else{
			$scope.selectView('topics');
		}
	}
	$scope.showGraph = function(values){
	}
});
twitter.run(function($rootScope, $http){
	$rootScope.data = [];
	$http.get('data/input.json').success(function(data){
		$rootScope.data = data;
	});
});
