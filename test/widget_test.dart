import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:baymax_companion/app.dart';

void main() {
  testWidgets('App launches with dashboard', (WidgetTester tester) async {
    await tester.pumpWidget(
      const ProviderScope(
        child: BaymaxCompanionApp(),
      ),
    );
    await tester.pumpAndSettle();

    expect(find.text('Dashboard'), findsWidgets);
  });
}
