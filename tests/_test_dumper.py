import textwrap
from collections import OrderedDict
from datetime import datetime, time
from decimal import Decimal
from uuid import UUID

import yaml
from django.test import TestCase
from django.utils.safestring import SafeString
from django.utils.timezone import utc
from rest_framework.exceptions import ErrorDetail
from rest_framework.relations import Hyperlink
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList

from drf_yaml import styles
from drf_yaml.encoders import SafeDumper


class _YAMLDumperTests(TestCase):
    """Tests specific to the YAML SafeDumper."""

    def test_bytes(self) -> None:
        """
        Test that Bytes are represented as YAML strings.

        Given:
            - A Bytes object
            - The YAML representation of that Bytes object as a string
        Do:
            - Render the Bytes object to YAML
        Expect:
            - The YAML string to be the same as the original YAML string
        """
        _yaml_repr = "bytes: abcd\n"

        obj = {"bytes": b"abcd"}

        yaml_repr = yaml.dump(
            obj,
            sort_keys=False,
            Dumper=SafeDumper,
            default_flow_style=False,
        )

        self.assertEqual(yaml_repr, _yaml_repr)

    def test_time(self) -> None:
        """
        Test that Times are represented as YAML strings.

        Given:
            - A Time
            - The YAML representation of that Time as a string
        Do:
            - Render the Time to YAML
        Expect:
            - The YAML string to be the same as the original YAML string
        """
        _yaml_repr = "time: '12:34:56'\n"

        obj = {"time": time(12, 34, 56)}

        yaml_repr = yaml.dump(
            obj,
            sort_keys=False,
            Dumper=SafeDumper,
            default_flow_style=False,
        )

        self.assertEqual(yaml_repr, _yaml_repr)

    def test_timedelta(self) -> None:
        """
        Test that Timedeltas are represented as YAML strings.

        Given:
            - A Timedelta
            - The YAML representation of that Timedelta as a string
        Do:
            - Render the Timedelta to YAML
        Expect:
            - The YAML string to be the same as the original YAML string
        """
        _yaml_repr = "timedelta: 97440.0\n"

        obj = {
            "timedelta": datetime(1, 1, 2, 3, 4, tzinfo=utc)
            - datetime(1, 1, 1, tzinfo=utc),
        }

        yaml_repr = yaml.dump(
            obj,
            sort_keys=False,
            Dumper=SafeDumper,
            default_flow_style=False,
        )

        self.assertEqual(yaml_repr, _yaml_repr)

    def test_decimal(self) -> None:
        """
        Test that Decimals are represented as YAML strings.

        Given:
            - A Decimal
            - The YAML representation of that Decimal as a string
        Do:
            - Render the Decimal to YAML
        Expect:
            - The YAML string to be the same as the original YAML string
        """
        _yaml_repr = "'123.456'\n"

        obj = Decimal("123.456")

        yaml_repr = yaml.dump(
            obj,
            sort_keys=False,
            Dumper=SafeDumper,
            default_flow_style=False,
        )

        self.assertEqual(yaml_repr, _yaml_repr)

    def test_uuid(self) -> None:
        """
        Test that UUIDs are represented as YAML strings.

        Given:
            - A UUID
            - The YAML representation of that UUID as a string
        Do:
            - Render the UUID to YAML
        Expect:
            - The YAML string to be the same as the original YAML string
        """
        _yaml_repr = "uuid: 12345678-1234-5678-1234-567812345678\n"

        obj = {"uuid": UUID("12345678-1234-5678-1234-567812345678")}

        yaml_repr = yaml.dump(
            obj,
            sort_keys=False,
            Dumper=SafeDumper,
            default_flow_style=False,
        )

        self.assertEqual(yaml_repr, _yaml_repr)

    def test_hyperlink(self) -> None:
        """
        Test that Hyperlinks are represented as YAML strings.

        Given:
            - A Hyperlink
            - The YAML representation of that Hyperlink as a string
        Do:
            - Render the Hyperlink to YAML
        Expect:
            - The YAML string to be the same as the original YAML string
        """
        _yaml_repr = "link: http://example.com\n"

        obj = {"link": Hyperlink("http://example.com", obj=None)}

        yaml_repr = yaml.dump(
            obj,
            sort_keys=False,
            Dumper=SafeDumper,
            default_flow_style=False,
        )

        self.assertEqual(yaml_repr, _yaml_repr)

    def test_error_detail(self) -> None:
        """
        Test that ErrorDetails are represented as YAML strings.

        Given:
            - An ErrorDetail
            - The YAML representation of that ErrorDetail as a string
        Do:
            - Render the ErrorDetail to YAML
        Expect:
            - The YAML string to be the same as the original YAML string
        """
        _yaml_repr = "error: foo\n"

        obj = {"error": ErrorDetail("foo")}

        yaml_repr = yaml.dump(
            obj,
            sort_keys=False,
            Dumper=SafeDumper,
            default_flow_style=False,
        )

        self.assertEqual(yaml_repr, _yaml_repr)

    def test_safe_string(self) -> None:
        """
        Test that SafeStrings are represented as YAML strings.

        Given:
            - A SafeString
            - The YAML representation of that SafeString as a string
        Do:
            - Render the SafeString to YAML
        Expect:
            - The YAML string to be the same as the original YAML string
        """
        _yaml_repr = "foo: bar\n"

        obj = {"foo": SafeString("bar")}

        yaml_repr = yaml.dump(
            obj,
            sort_keys=False,
            Dumper=SafeDumper,
            default_flow_style=False,
        )

        self.assertEqual(yaml_repr, _yaml_repr)

    def test_ordered_dict(self) -> None:
        """
        Test that OrderedDicts are represented as YAML mappings.

        Given:
            - A simple ordered dict
            - The YAML representation of that dict as a string
        Do:
            - Render the dict to YAML
        Expect:
            - The YAML string to be the same as the original YAML string
        """
        _yaml_repr = "foo:\n- bar\n- baz\n"

        obj = OrderedDict({"foo": ["bar", "baz"]})

        self.assertEqual(
            yaml.dump(
                obj,
                sort_keys=False,
                Dumper=SafeDumper,
                default_flow_style=False,
            ),
            _yaml_repr,
        )

    def test_return_dict(self) -> None:
        """
        Test that ReturnDicts are represented as YAML mappings.

        Given:
            - A ReturnDict
            - The YAML representation of that ReturnDict as a string
        Do:
            - Render the ReturnDict to YAML
        Expect:
            - The YAML string to be the same as the original YAML string
        """
        _yaml_repr = "foo:\n- bar\n- baz\n"

        obj = ReturnDict({"foo": ["bar", "baz"]}, serializer=None)

        yaml_repr = yaml.dump(
            obj,
            sort_keys=False,
            Dumper=SafeDumper,
            default_flow_style=False,
        )

        self.assertEqual(yaml_repr, _yaml_repr)

    def test_return_list(self) -> None:
        """
        Test that ReturnLists are represented as YAML sequences.

        Given:
            - A ReturnList
            - The YAML representation of that ReturnList as a string
        Do:
            - Render the ReturnList to YAML
        Expect:
            - The YAML string to be the same as the original YAML string
        """
        _yaml_repr = "- foo\n- bar\n- baz\n"

        obj = ReturnList(["foo", "bar", "baz"], serializer=None)

        yaml_repr = yaml.dump(
            obj,
            sort_keys=False,
            Dumper=SafeDumper,
            default_flow_style=False,
        )

        self.assertEqual(yaml_repr, _yaml_repr)

    def test_generator_type(self) -> None:
        """
        Test that GeneratorTypes are represented as YAML sequences.

        Given:
            - A GeneratorType
            - The YAML representation of that GeneratorType as a string
        Do:
            - Render the GeneratorType to YAML
        Expect:
            - The YAML string to be the same as the original YAML string
        """
        _yaml_repr = "- foo\n- bar\n- baz\n"

        obj = (item for item in ["foo", "bar", "baz"])

        yaml_repr = yaml.dump(
            obj,
            sort_keys=False,
            Dumper=SafeDumper,
            default_flow_style=False,
        )

        self.assertEqual(yaml_repr, _yaml_repr)

    def test_folded_str(self) -> None:
        """
        Test that folded strings are represented as YAML folded strings.

        Given:
            - A folded string
            - The YAML representation of that string as a string
        Do:
            - Render the string to YAML
        Expect:
            - The YAML string to be the same as the original YAML string
        """
        _yaml_repr = "foo: >-\n  bar\n\n  baz\n"

        obj = {"foo": styles.FoldedStr("bar\nbaz")}

        yaml_repr = yaml.dump(
            obj,
            sort_keys=False,
            Dumper=SafeDumper,
            default_flow_style=False,
        )

        self.assertEqual(yaml_repr, _yaml_repr)

    def test_literal_str(self) -> None:
        """
        Test that literal strings are represented as YAML literal strings.

        Given:
            - A literal string
            - The YAML representation of that string as a string
        Do:
            - Render the string to YAML
        Expect:
            - The YAML string to be the same as the original YAML string
        """
        _yaml_repr = "foo: |-\n  bar\n  baz\n"

        obj = {"foo": styles.LiteralStr("bar\nbaz")}

        yaml_repr = yaml.dump(
            obj,
            sort_keys=False,
            Dumper=SafeDumper,
            default_flow_style=False,
        )

        self.assertEqual(yaml_repr, _yaml_repr)

    def test_single_quoted_str(self) -> None:
        """
        Test that single quoted strings are represented as YAML single quoted strings.

        Given:
            - A single quoted string
            - The YAML representation of that string as a string
        Do:
            - Render the string to YAML
        Expect:
            - The YAML string to be the same as the original YAML string
        """
        _yaml_repr = "foo: 'bar'\n"

        obj = {"foo": styles.SingleQuotedStr("bar")}

        yaml_repr = yaml.dump(
            obj,
            sort_keys=False,
            Dumper=SafeDumper,
            default_flow_style=False,
        )

        self.assertEqual(yaml_repr, _yaml_repr)

    def test_double_quoted_str(self) -> None:
        """
        Test that double quoted strings are represented as YAML double quoted strings.

        Given:
            - A double quoted string
            - The YAML representation of that string as a string
        Do:
            - Render the string to YAML
        Expect:
            - The YAML string to be the same as the original YAML string
        """
        _yaml_repr = 'foo: "bar"\n'

        obj = {"foo": styles.DoubleQuotedStr("bar")}

        yaml_repr = yaml.dump(
            obj,
            sort_keys=False,
            Dumper=SafeDumper,
            default_flow_style=False,
        )

        self.assertEqual(yaml_repr, _yaml_repr)

    def test_flow_style_sequence(self) -> None:
        """
        Test that flow style sequences are represented as YAML flow style sequences.

        Given:
            - A flow style sequence
            - The YAML representation of that sequence as a string
        Do:
            - Render the sequence to YAML
        Expect:
            - The YAML string to be the same as the original YAML string
        """
        _yaml_repr = textwrap.dedent(
            """
            flowing: [bar, baz]
            not-flowing:
            - bar
            - baz
            """,
        ).lstrip()

        obj = {
            "flowing": styles.FlowStyleSequence(["bar", "baz"]),
            "not-flowing": ["bar", "baz"],
        }

        yaml_repr = yaml.dump(
            obj,
            sort_keys=False,
            Dumper=SafeDumper,
            default_flow_style=False,
        )

        self.assertEqual(yaml_repr, _yaml_repr)

    def test_flow_style_mapping(self) -> None:
        """
        Test that flow style mappings are represented as YAML flow style mappings.

        Given:
            - A flow style mapping
            - The YAML representation of that mapping as a string
        Do:
            - Render the mapping to YAML
        Expect:
            - The YAML string to be the same as the original YAML string
        """
        _yaml_repr = textwrap.dedent(
            """
            flowing: {foo: bar, baz: qux}
            not-flowing:
              foo: bar
              baz: qux
            """,
        ).lstrip()

        obj = {
            "flowing": styles.FlowStyleMapping({"foo": "bar", "baz": "qux"}),
            "not-flowing": {"foo": "bar", "baz": "qux"},
        }

        yaml_repr = yaml.dump(
            obj,
            sort_keys=False,
            Dumper=SafeDumper,
            default_flow_style=False,
        )

        self.assertEqual(yaml_repr, _yaml_repr)
