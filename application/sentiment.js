var twitter = angular.module('myApp', ['ui.bootstrap','nvd3ChartDirectives']);

twitter.controller('myController', function($rootScope, $scope){
	$scope.view = "";
	$scope.graphID = "active";
	$scope.selectView = function(view){
		$scope.view = view;
		$scope.graphData = [];
		$scope.selectedGraphs = [];
		$scope.selectedCountries = [];
		$scope.selectedTopics = [];
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
				$scope.topics.push(value.value);
			});
		}
	};

	$scope.$watch('graphData', function(){
	},true);
	$scope.graphData = [];
	$scope.selectedGraphs = [];
	$scope.selectedCountries = [];
	$scope.selectedTopics = [];
	
	$scope.selectTopic = function(index){
		$scope.selectedData.topic = {
			value: $scope.data[index].value,
			index: index
		}
		var duplicate = false;
		var dpos = "";
		if($scope.selectedData.country){
			var i = 0;
			angular.forEach($scope.selectedGraphs, function(v, k){
				if(v.key == $scope.selectedData.topic.value){
					duplicate = true;
					dpos = i;
				}
				i++;
			})
			if(duplicate == false){
				var cindex = $scope.selectedData.country.index;
				$scope.selectedTopics[$scope.selectedData.topic.value] = true;
				$scope.selectedData.values = $scope.data[index].content[cindex].rates;
				var rpos = $scope.selectedData.values.positive / ($scope.selectedData.values.positive + $scope.selectedData.values.negative) * 100;
				var rneg = $scope.selectedData.values.negative / ($scope.selectedData.values.positive + $scope.selectedData.values.negative) * 100;
				var data = 	{
						key: $scope.selectedData.topic.value,
						values: [[ "positiv", rpos ],[ "negativ", rneg ]]
					}
				$scope.selectedGraphs.push(data);
				$scope.graphData = angular.copy($scope.selectedGraphs);
			}else{
				$scope.selectedTopics[$scope.selectedData.topic.value] = false;
				$scope.selectedGraphs.splice(dpos, 1);
				$scope.graphData = angular.copy($scope.selectedGraphs);
			}
		}else{
			$scope.selectView('countries');
		}
	}
	$scope.showCountries = function(){
		if(!$scope.countries.length){
			var dupe = 0;
			angular.forEach($scope.data, function(data){

				angular.forEach(data.content, function(c) {
					angular.forEach($scope.countries, function(v){
						if(v == c.value){
							dupe = 1;
						}
					});
					if(dupe == 0){
						$scope.countries.push(c.value);
					}
				});
			});
		}
		if($scope.countries.length && $scope.selectedData.topic){
			$scope.countries = [];
			angular.forEach($scope.data, function(d){
				if(d.value == $scope.selectedData.topic.value){
					angular.forEach(d.content, function(c){
						$scope.countries.push(c.value);
					})
				}
			});
		}
	};
	
	$scope.selectCountry = function(index){
		$scope.selectedData.country = {
			value: $scope.countries[index],
			index: index
		}
		var duplicate = false;
		var dpos = "";
		if($scope.selectedData.topic){
			var i = 0;
			angular.forEach($scope.selectedGraphs, function(v, k){
				if(v.key == $scope.selectedData.country.value){
					duplicate = true;
					dpos = i;
				}
				i++;
			})
			if(duplicate == false){	
				var tindex = $scope.selectedData.topic.index;
				$scope.selectedCountries[$scope.selectedData.country.value] = true;
				$scope.selectedData.values = $scope.data[tindex].content[index].rates;
				var rpos = $scope.selectedData.values.positive / ($scope.selectedData.values.positive + $scope.selectedData.values.negative) * 100;
				var rneg = $scope.selectedData.values.negative / ($scope.selectedData.values.positive + $scope.selectedData.values.negative) * 100;
				var data = 	{
						key: $scope.selectedData.country.value,
						values: [[ "positiv",  rpos ],[  "negativ",  rneg ]]
					}
				$scope.selectedGraphs.push(data);
				$scope.graphData = angular.copy($scope.selectedGraphs);
			}else{
				$scope.selectedCountries[$scope.selectedData.country.value] = false;
				$scope.selectedGraphs.splice(dpos, 1);
				$scope.graphData = angular.copy($scope.selectedGraphs);
			}
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
