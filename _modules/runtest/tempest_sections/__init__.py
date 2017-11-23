
import auth
import baremetal
import baremetal_feature_enabled
import compute
import compute_feature_enabled
import debug
import default
import dns
import dns_feature_enabled
import heat_plugin
import identity
import identity_feature_enabled
import image
import image_feature_enabled
import network
import network_feature_enabled
import object_storage
import object_storage_feature_enabled
import orchestration
import oslo_concurrency
import scenario
import service_clients
import service_available
import validation
import volume
import volume_feature_enabled

SECTIONS = [
    auth.Auth,
    baremetal.Baremetal,
    baremetal_feature_enabled.BaremetalFeatureEnabled,
    compute.Compute,
    compute_feature_enabled.ComputeFeatureEnabled,
    debug.Debug,
    default.Default,
    dns.Dns,
    dns_feature_enabled.DnsFeatureEnabled,
    heat_plugin.HeatPlugin,
    identity.Identity,
    identity_feature_enabled.IdentityFeatureEnabled,
    image.Image,
    image_feature_enabled.ImageFeatureEnabled,
    network.Network,
    network_feature_enabled.NetworkFeatureEnabled,
    object_storage.ObjectStorage,
    object_storage_feature_enabled.ObjectStorageFeatureEnabled,
    orchestration.Orchestration,
    oslo_concurrency.OsloConcurrency,
    scenario.Scenario,
    service_clients.ServiceClients,
    service_available.ServiceAvailable,
    validation.Validation,
    volume.Volume,
    volume_feature_enabled.VolumeFeatureEnabled,
]
