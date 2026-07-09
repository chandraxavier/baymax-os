import 'package:dio/dio.dart';

import '../config/app_config.dart';
import '../constants/app_constants.dart';

class ApiClient {
  ApiClient({String? baseUrl})
      : _dio = Dio(
          BaseOptions(
            baseUrl: baseUrl ?? AppConfig.apiBaseUrl,
            connectTimeout: AppConstants.networkTimeout,
            receiveTimeout: AppConstants.networkTimeout,
            headers: const {'Content-Type': 'application/json'},
          ),
        );

  final Dio _dio;

  Dio get dio => _dio;
}
