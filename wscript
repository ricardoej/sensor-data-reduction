# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

# def options(opt):
#     pass

# def configure(conf):
#     conf.check_nonfatal(header_name='stdint.h', define_name='HAVE_STDINT_H')

def build(bld):
    module = bld.create_ns3_module('sensor-data-reduction', ['core'])
    module.source = [
        'model/sensor-data-reduction.cc',
        'helper/sensor-data-reduction-helper.cc',
        ]

    module_test = bld.create_ns3_module_test_library('sensor-data-reduction')
    module_test.source = [
        'test/sensor-data-reduction-test-suite.cc',
        ]

    headers = bld(features='ns3header')
    headers.module = 'sensor-data-reduction'
    headers.source = [
        'model/sensor-data-reduction.h',
        'helper/sensor-data-reduction-helper.h',
        ]

    if bld.env.ENABLE_EXAMPLES:
        bld.recurse('examples')

    # bld.ns3_python_bindings()

